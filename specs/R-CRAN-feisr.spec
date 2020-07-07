%global packname  feisr
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Estimating Fixed Effects Individual Slope Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-aod 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-aod 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 

%description
Provides the function feis() to estimate fixed effects individual slope
(FEIS) models. The FEIS model constitutes a more general version of the
often-used fixed effects (FE) panel model, as implemented in the package
'plm' by Croissant and Millo (2008) <doi:10.18637/jss.v027.i02>. In FEIS
models, data are not only person demeaned like in conventional FE models,
but detrended by the predicted individual slope of each person or group.
Estimation is performed by applying least squares lm() to the transformed
data. For more details on FEIS models see Bruederl and Ludwig (2015,
ISBN:1446252442); Frees (2001) <doi:10.2307/3316008>; Polachek and Kim
(1994) <doi:10.1016/0304-4076(94)90075-2>; Ruettenauer and Ludwig (2020)
<doi:10.1177/0049124120926211>; Wooldridge (2010, ISBN:0262294354). To
test consistency of conventional FE and random effects estimators against
heterogeneous slopes, the package also provides the functions feistest()
for an artificial regression test and bsfeistest() for a bootstrapped
version of the Hausman test.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
