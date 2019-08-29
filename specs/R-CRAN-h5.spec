%global packname  h5
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}
Summary:          Interface to the 'HDF5' Library

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    hdf5-devel >= 1.8.12
Requires:         hdf5
BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-methods 

%description
S4 Interface to the 'HDF5' library supporting fast storage and retrieval
of R-objects like vectors, matrices and arrays to binary files in a
language independent format. The 'HDF5' format can therefore be used as an
alternative to R's save/load mechanism. Since h5 is able to access only
subsets of stored data it can also handle data sets which do not fit into
memory.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/benchmark
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/h5ex_t_enum.h5
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/test-ascii-length-bug.h5
%doc %{rlibdir}/%{packname}/test-ascii-length-bug.py
%doc %{rlibdir}/%{packname}/test-f32.h5
%doc %{rlibdir}/%{packname}/test-f32.py
%doc %{rlibdir}/%{packname}/test-h5link.h5
%doc %{rlibdir}/%{packname}/test-h5link.py
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
