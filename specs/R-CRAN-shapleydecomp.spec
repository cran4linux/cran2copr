%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shapleydecomp
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shapley Value Decomposition for Discrete-Time Simulation Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-parallel 
Requires:         R-utils 

%description
Attributes changes in the outcomes of a discrete-time simulation model to
its input factors using Shapley values (Shapley 1953)
<doi:10.1515/9781400881970-018>, which for binary factors coincide with
the symmetric standardization of Das Gupta (1993)
<https://www2.census.gov/library/publications/1993/demographics/p23-186.pdf>.
Any calibrated model can be decomposed by implementing four S3 methods
that run the model, summarize its output, and construct counterfactual
inputs. Counterfactuals either remove a factor entirely or hold it at its
value in a baseline year, and a sequential decomposition attributes each
year's policy conditional on the past.

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
