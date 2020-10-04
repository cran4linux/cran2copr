%global packname  difR
%global packver   5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Collection of Methods to Detect Dichotomous Differential ItemFunctioning (DIF)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-deltaPlotR 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-deltaPlotR 

%description
Provides a collection of standard methods to detect differential item
functioning among dichotomously scored items. Methods for uniform and
non-uniform DIF, based on test-score or IRT methods, for comparing two or
more than two groups of respondents, are available (Magis, Beland,
Tuerlinckx and De Boeck,A General Framework and an R Package for the
Detection of Dichotomous Differential Item Functioning, Behavior Research
Methods, 42, 2010, 847-862 <doi:10.3758/BRM.42.3.847>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
