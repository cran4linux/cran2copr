%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datanugget
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create, Optimize, and Refine Data Nuggets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 4.0.5
BuildRequires:    R-CRAN-ggplot2 >= 4.0.2
BuildRequires:    R-CRAN-Rfast >= 2.0.7
BuildRequires:    R-CRAN-mgcv >= 1.9.4
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-doParallel >= 1.0.17
BuildRequires:    R-CRAN-doSNOW >= 1.0.16
Requires:         R-parallel >= 4.0.5
Requires:         R-CRAN-ggplot2 >= 4.0.2
Requires:         R-CRAN-Rfast >= 2.0.7
Requires:         R-CRAN-mgcv >= 1.9.4
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-doSNOW >= 1.0.16

%description
Creating, optimizing and refining data nuggets. Data nuggets reduce a
large dataset into a small collection of nuggets of data, each containing
a center (location), weight (importance), and scale (variability)
parameter. Data nugget centers are selected based on a space-filling
maximum-entropy scheme. Data nugget weights are created by counting the
number observations closest to a given data nugget center. We then say the
data nugget 'contains' these observations and the data nugget center is
recalculated as the mean of these observations. Data nugget scales are
created by calculating the trace of the covariance matrix of the
observations contained within a data nugget divided by the dimension of
the dataset. The optimal number of data nuggets is determined data-driven
based on the relative second-order differences of propensity score
indices. Data nuggets are refined by 'splitting' data nuggets which have
high scales or elongated shapes (defined as the ratio of the two largest
eigenvalues of the covariance matrix of the observations contained within
the data nugget).

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
