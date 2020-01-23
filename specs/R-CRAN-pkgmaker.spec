%global packname  pkgmaker
%global packver   0.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.31
Release:          1%{?dist}
Summary:          Development Utilities for R Packages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bibtex >= 0.4
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-registry 
BuildRequires:    R-tools 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-codetools 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-bibtex >= 0.4
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-registry 
Requires:         R-tools 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-codetools 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-assertthat 

%description
Provides some low-level utilities to use for package development. It
currently provides managers for multiple package specific options and
registries, vignette, unit test and bibtex related utilities. It serves as
a base package for packages like NMF, RcppOctave, doRNG, and as an
incubator package for other general purposes utilities, that will
eventually be packaged separately. It is still under heavy development and
changes in the interface(s) are more than likely to happen.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/cleveref.sty
%doc %{rlibdir}/%{packname}/package.mk
%doc %{rlibdir}/%{packname}/vignette.mk
%{rlibdir}/%{packname}/INDEX
