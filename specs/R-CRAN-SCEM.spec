%global __brp_check_rpaths %{nil}
%global packname  SCEM
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Splitting-Coalescence-Estimation Method

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mathjaxr 
Requires:         R-CRAN-devtools 
Requires:         R-stats 
Requires:         R-CRAN-mathjaxr 

%description
We introduce improved methods for statistically assessing birth
seasonality and intra-annual variation. The first method we propose is a
new idea that uses a nonparametric clustering procedure to group
individuals with similar time series data and estimate birth seasonality
based on the clusters. One can use the function SCEM() to implement this
method. The second method estimates input parameters for use with a
previously-developed parametric approach (Tornero et al., 2013). The
relevant code for this approach is makeFits_OLS(), while
makeFits_initial() is the code to implement the same method but with given
initial conditions for two parameters. The latter can be used to show the
disadvantage of the existing approach. One can use the function makeFits()
to generate parametric birth seasonality estimates using either
initialization. Detailed description can be found here: Chazin Hannah,
Soudeep Deb, Joshua Falk, and Arun Srinivasan. (2019) "New Statistical
Approaches to Intra-Individual Isotopic Analysis and Modeling Birth
Seasonality in Studies of Herd Animals." <doi:10.1111/arcm.12432>.

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
