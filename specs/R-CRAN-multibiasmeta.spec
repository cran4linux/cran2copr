%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multibiasmeta
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis for Multiple Biases in Meta-Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-EValue 
BuildRequires:    R-CRAN-metabias 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-robumeta 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-EValue 
Requires:         R-CRAN-metabias 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-robumeta 

%description
Meta-analyses can be compromised by studies' internal biases (e.g.,
confounding in nonrandomized studies) as well as by publication bias. This
package conducts sensitivity analyses for the joint effects of these
biases (per Mathur (2022) <doi:10.31219/osf.io/u7vcb>). These sensitivity
analyses address two questions: (1) For a given severity of internal bias
across studies and of publication bias, how much could the results
change?; and (2) For a given severity of publication bias, how severe
would internal bias have to be, hypothetically, to attenuate the results
to the null or by a given amount?

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
