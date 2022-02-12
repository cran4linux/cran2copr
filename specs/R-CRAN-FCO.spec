%global __brp_check_rpaths %{nil}
%global packname  FCO
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Cutoffs for Model Fit Evaluation in Covariance-Based Structural Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-semTools 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-semTools 
Requires:         R-parallel 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 

%description
A toolbox to derive flexible cutoffs for fit indices in 'Covariance-based
Structural Equation Modeling' based on the paper by 'Niemand & Mai (2018)'
<doi:10.1007/s11747-018-0602-9>. Flexible cutoffs are an alternative to
fixed cutoffs - rules-of-thumb - regarding an appropriate cutoff for fit
indices such as 'CFI' or 'SRMR'. It has been demonstrated that these
flexible cutoffs perform better than fixed cutoffs in grey areas where
misspecification is not easy to detect. The package provides an
alternative to the tool at <https://flexiblecutoffs.org> as it allows to
tailor flexible cutoffs to a given dataset and model, which is so far not
available in the tool. The package simulates fit indices based on a given
dataset and model and then estimates the flexible cutoffs. Some useful
functions, e.g., to determine the 'GoF-' or 'BoF-nature' of a fit index,
are provided. So far, additional options for a relative use (is a model
better than another?) are provided in an exploratory manner.

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
