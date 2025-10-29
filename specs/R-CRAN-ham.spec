%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ham
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Healthcare Analysis Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Conducts analyses for healthcare program evaluations or intervention
studies. Calculates regression analyses for standard ordinary least
squares (OLS or linear) or logistic models. Performs regression models
used for causal modeling such as differences-in-differences (DID) and
interrupted time series (ITS) models. Provides limited interpretations of
model results and a ranking of variable importance in models. Performs
propensity score models, top-coding of model outcome variables, and can
return new data with the newly formed variables. Also performs Cronbach's
alpha for various scale items (e.g., survey questions). See Github URL for
examples in the README file. For more details on the statistical methods,
see Allen & Yen (1979, ISBN:0-8185-0283-5), Angrist & Pischke (2009,
ISBN:9780691120355), Harrell (2016, ISBN:978-3-319-19424-0), Kline (1999,
ISBN:9780415211581), Linden (2015) <doi:10.1177/1536867X1501500208>, Merlo
(2006) <doi:10.1136/jech.2004.029454> Muthen & Satorra (1995)
<doi:10.2307/271070>, and Rabe-Hesketh & Skrondal (2008,
ISBN:978-1-59718-040-5).

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
