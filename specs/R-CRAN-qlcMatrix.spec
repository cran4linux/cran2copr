%global __brp_check_rpaths %{nil}
%global packname  qlcMatrix
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          3%{?dist}%{?buildtag}
Summary:          Utility Sparse Matrix Functions for Quantitative LanguageComparison

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-Matrix >= 1.1.0
BuildRequires:    R-CRAN-slam >= 0.1.32
BuildRequires:    R-CRAN-sparsesvd 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-docopt 
Requires:         R-Matrix >= 1.1.0
Requires:         R-CRAN-slam >= 0.1.32
Requires:         R-CRAN-sparsesvd 
Requires:         R-methods 
Requires:         R-CRAN-docopt 

%description
Extension of the functionality of the Matrix package for using sparse
matrices. Some of the functions are very general, while other are highly
specific for special data format as used for quantitative language
comparison (QLC).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
