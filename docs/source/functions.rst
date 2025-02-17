*********
Functions
*********

.. _savefig():

savefig()
=========

Saves the current plot as PyPDF file.

.. code:: python

    savefig(fname, 
            pack_list = [],
            cleanup = True,
            multiple = 'pickle',
            force_pickle = False,
            verbose = True
            prompt_overwrite = False,
            **kwargs)


:fname: *str*

   Filename of the output file.

:pack_list: *list*, default = ``[]`` 
  
  List with filenames that will be embedded in the PyPDF-file. The generating script is added separately and should not be included here. See :ref:`Packing and unpacking` for more details.

:multiple: *str*, default = ``'pickle'`` 
 
  How to handle multiple plots in a single generating script. Can be any of ``'pickle'``, ``'add_page'``, or ``'finalize'``. See :ref:`Multiple plots` for more details
 
:cleanup: *bool*, default = ``True`` 

   Whether or not to cleanup files that have been embedded in the PyPDF file. Set to ``False`` and run script to extract embedded files.

:force_pickle: *bool*, default = ``False`` 
  
  Pickles the figure and embeds a Python script that unpickles and reads the figure again. This can be useful when dealing with very large source files, see :ref:`Pickling` for more details.

:verbose: *bool*, default = ``True`` 

  Wether or not to show verbose comments during saving.
  
:prompt_overwrite: *bool*, default = ``False`` 
  
  Wether or not to prompt when the output file already exists and is about to be overwritten. If ``False`` and the output file does already exist, file will be overwritten if possible.
  
:\*\*kwargs: Any keyword arguments accepted by ``matplotlib.pyplot.savefig()``

unpack()
=========

Extracts the files embedded in the PyPDF-file. Must be called before embedded files are read by the generating script. This can be guaranteed by importing the backend using ``pypdfplot.backend.unpack``, which automatically calls ``unpack()`` with its default parameters. See :ref:`Packing and unpacking` for more details.


.. code:: python

    unpack(fname = None,
           verbose = True)

:fname: *str*, default = ``None``

   Filename of the PyPDF file to unpack. If ``None``, the filename of the currently executing script is taken.
   
:verbose: *bool*, default = ``True`` 

  Wether or not to show verbose comments during extraction.

            
fix_pypdf()
===========

Fixes PyPDF files that have been severed, e.g. because they were saved as 'regular' PDF-files outside of ``pypdfplot``. See :ref:`PyPDF compliance types` for more details.

.. code:: python

    fix_pypdf(input_fname,
              output_fname = None,
              verbose = True)

:input_fname: *str*

   Filename of the severed PyPDF file
   
:output_fname: *str*, default = ``None``

   Filename of the fixed output PyPDF file. If ``None``, the input PDF file is overwritten.
      
:verbose: *bool*, default = ``True`` 

  Wether or not to show verbose comments during fixing.

