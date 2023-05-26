%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  optical
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Item Calibration

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
The restricted optimal design method is implemented to optimally allocate
a set of items that require calibration to a group of examinees. The
optimization process is based on the method described in detail by Ul
Hassan and Miller in their works published in (2019)
<doi:10.1177/0146621618824854> and (2021)
<doi:10.1016/j.csda.2021.107177>. To use the method, preliminary item
characteristics must be provided as input. These characteristics can
either be expert guesses or based on previous calibration with a small
number of examinees. The item characteristics should be described in the
form of parameters for an Item Response Theory (IRT) model. These models
can include the Rasch model, the 2-parameter logistic model, the
3-parameter logistic model, or a mixture of these models. The output
consists of a set of rules for each item that determine which examinees
should be assigned to each item. The efficiency or gain achieved through
the optimal design is quantified by comparing it to a random allocation.
This comparison allows for an assessment of how much improvement or
advantage is gained by using the optimal design approach. This work was
supported by the Swedish Research Council (Vetenskapsrådet) Grant
2019-02706.

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
