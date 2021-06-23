%global __brp_check_rpaths %{nil}
%global packname  bazar
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          3%{?dist}%{?buildtag}
Summary:          Miscellaneous Basic Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-kimisc 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-kimisc 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
A collection of miscellaneous functions for copying objects to the
clipboard ('Copy'); manipulating strings ('concat', 'mgsub', 'trim',
'verlan'); loading or showing packages ('library_with_dep',
'require_with_dep', 'sessionPackages'); creating or testing for named
lists ('nlist', 'as.nlist', 'is.nlist'), formulas ('is.formula'), empty
objects ('as.empty', 'is.empty'), whole numbers ('as.wholenumber',
'is.wholenumber'); testing for equality ('almost.equal', 'almost.zero')
and computing uniqueness ('almost.unique'); getting modified versions of
usual functions ('rle2', 'sumNA'); making a pause or a stop ('pause',
'stopif'); converting into a function ('as.fun'); providing a C like
ternary operator ('condition %?% true %:% false'); finding packages and
functions ('get_all_pkgs', 'get_all_funs'); and others ('erase', '%nin%',
'unwhich', 'top', 'bot', 'normalize').

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
