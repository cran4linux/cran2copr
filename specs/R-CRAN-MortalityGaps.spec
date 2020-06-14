%global packname  MortalityGaps
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          The Double-Gap Life Expectancy Forecasting Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-crch 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-forecast 
Requires:         R-MASS 
Requires:         R-CRAN-crch 
Requires:         R-CRAN-pbapply 

%description
Life expectancy is highly correlated over time among countries and between
males and females. These associations can be used to improve forecasts.
Here we have implemented a method for forecasting female life expectancy
based on analysis of the gap between female life expectancy in a country
compared with the record level of female life expectancy in the world.
Second, to forecast male life expectancy, the gap between male life
expectancy and female life expectancy in a country is analysed. We named
this method the Double-Gap model. For a detailed description of the method
see Pascariu et al. (2017). <doi:10.1016/j.insmatheco.2017.09.011>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
