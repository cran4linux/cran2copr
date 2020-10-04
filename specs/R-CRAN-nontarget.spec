%global packname  nontarget
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          3%{?dist}%{?buildtag}
Summary:          Detecting Isotope, Adduct and Homologue Relations in LC-MS Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-enviPat >= 2.0
BuildRequires:    R-mgcv >= 1.7.22
BuildRequires:    R-CRAN-nontargetData >= 1.1
Requires:         R-CRAN-enviPat >= 2.0
Requires:         R-mgcv >= 1.7.22
Requires:         R-CRAN-nontargetData >= 1.1

%description
Screening a HRMS data set for peaks related by (1) isotope patterns, (2)
different adducts of the same molecule and/or (3) homologue series. The
resulting isotopic pattern and adduct groups can then be combined to
so-called components, with homologue series information attached. Also
allows plotting and filtering HRMS data for mass defects, frequent m/z
distances and components vs. non-components.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
