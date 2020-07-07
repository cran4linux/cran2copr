%global packname  MLRShiny2
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Interactive Application for Working with Multiple LinearRegression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-QuantPsyc 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-corrgram 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-QuantPsyc 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-corrgram 

%description
An interactive application for working with multiple linear regression
technique. The application has a template for solving problems on multiple
linear regression. Runtime examples are provided at
<https://kartikeyastat.shinyapps.io/MLR_WEB_K/>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
