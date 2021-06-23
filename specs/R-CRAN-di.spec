%global __brp_check_rpaths %{nil}
%global packname  di
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Deficit Index (DI)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-scales 

%description
A set of utilities for calculating the Deficit (frailty) Index (DI) in
gerontological studies. The deficit index was first proposed by Arnold
Mitnitski and Kenneth Rockwood and represents a proxy measure of aging and
also can be served as a sensitive predictor of survival. For more
information, see (i)"Accumulation of Deficits as a Proxy Measure of Aging"
by Arnold B. Mitnitski et al. (2001), The Scientific World Journal 1,
<DOI:10.1100/tsw.2001.58>; (ii) "Frailty, fitness and late-life mortality
in relation to chronological and biological age" by Arnold B Mitnitski et
al. (2001), BMC Geriatrics2002 2(1), <DOI:10.1186/1471-2318-2-1>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
