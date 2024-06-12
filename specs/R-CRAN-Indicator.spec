%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Indicator
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Composite 'Indicator' Construction and Imputation Data

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-missMethods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-norm 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-missMethods 
Requires:         R-stats 
Requires:         R-CRAN-norm 

%description
Different functions includes constructing composite indicators, imputing
missing data, and evaluating imputation techniques. Additionally,
different tools for data normalization. Detailed methodologies of
'Indicator' package are: OECD/European Union/EC-JRC (2008), "Handbook on
Constructing Composite Indicators: Methodology and User Guide", OECD
Publishing, Paris, <DOI:10.1787/533411815016>, Matteo Mazziotta & Adriano
Pareto, (2018) "Measuring Well-Being Over Time: The Adjusted
Mazziotta–Pareto Index Versus Other Non-compensatory Indices"
<DOI:10.1007/s11205-017-1577-5> and De Muro P., Mazziotta M., Pareto A.
(2011), "Composite Indices of Development and Poverty: An Application to
MDGs" <DOI:10.1007/s11205-010-9727-z>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
