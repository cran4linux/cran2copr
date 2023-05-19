%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  idmact
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interpreting Differences Between Mean ACT Scores

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-rlang 

%description
Interpreting the differences between mean scale scores across various
forms of an assessment can be challenging. This difficulty arises from
different mappings between raw scores and scale scores, complex
mathematical relationships, adjustments based on judgmental procedures,
and diverse equating functions applied to different assessment forms. An
alternative method involves running simulations to explore the effect of
incrementing raw scores on mean scale scores. The 'idmact' package
provides an implementation of this approach based on the algorithm
detailed in Schiel (1998)
<https://www.act.org/content/dam/act/unsecured/documents/ACT_RR98-01.pdf>
which was developed to help interpret differences between mean scale
scores on the American College Testing (ACT) assessment. The function
idmact_subj() within the package offers a framework for running
simulations on subject-level scores. In contrast, the idmact_comp()
function provides a framework for conducting simulations on composite
scores.

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
