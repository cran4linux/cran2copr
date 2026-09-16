%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autorelevate
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Autorelevated Family of Probability Distributions and Estimation Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Implements the autorelevated family of probability distributions, obtained
by applying the autorelevation transformation of Krakowski (1973)
<doi:10.1051/ro/197307V201071> and Dileepkumar and Sankaran (2022) to ten
baseline probability distributions: Weibull, Lomax, Burr XII, Gompertz,
Log-Logistic, Chen, Exponentiated Exponential, Power Lindley, Log-normal,
and Gamma. The Weibull member of the family is studied in detail by Dileep
Kumar, Shabeer, and Sankaran (2025) <doi:10.1080/01966324.2026.2665479>.
The Lomax member is studied by Sharma, Pal, Bhardwaj, and Tyagi (2026,
submitted), who establish its upside-down bathtub hazard shape. Supplies
vectorized density, distribution, survival, hazard, quantile (via the
negative branch of the Lambert W function), and random-generation
functions for all ten members of the family. It also implements Maximum
Likelihood, Maximum Product of Spacings, Least Squares, Weighted Least
Squares, and Cramer-von Mises estimation methods along with a
Kolmogorov-Smirnov goodness-of-fit test, a Total Time on Test plot, and
model selection by AIC, BIC, CAIC, and HQIC. It also includes a bundled
bladder cancer remission dataset (Lee and Wang, 2003) for illustration.

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
