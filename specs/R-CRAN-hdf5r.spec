%global packname  hdf5r
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Interface to the 'HDF5' Binary Data Format

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    hdf5-devel >= 1.8.13
Requires:         hdf5
BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-bit64 
Requires:         R-utils 

%description
'HDF5' is a data model, library and file format for storing and managing
large amounts of data. This package provides a nearly feature complete,
object oriented wrapper for the 'HDF5' API
<https://support.hdfgroup.org/HDF5/doc/RM/RM_H5Front.html> using R6
classes. Additionally, functionality is added so that 'HDF5' objects
behave very similar to their corresponding R counterparts.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CWrappers_1.10.2
%doc %{rlibdir}/%{packname}/CWrappers_1.10.3
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/h5ex_t_enum.h5
%doc %{rlibdir}/%{packname}/HDF5_COPYRIGHTS.txt
%doc %{rlibdir}/%{packname}/m4
%doc %{rlibdir}/%{packname}/test-ascii-length-bug.h5
%doc %{rlibdir}/%{packname}/test-ascii-length-bug.py
%doc %{rlibdir}/%{packname}/test-f32.h5
%doc %{rlibdir}/%{packname}/test-h5link.h5
%doc %{rlibdir}/%{packname}/test-h5link.py
%doc %{rlibdir}/%{packname}/test-scalar.h5
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
