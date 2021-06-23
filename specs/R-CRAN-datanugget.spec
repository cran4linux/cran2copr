%global __brp_check_rpaths %{nil}
%global packname  datanugget
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create, Refine, and Cluster Data Nuggets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.5.0
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-doSNOW >= 1.0.16
Requires:         R-parallel >= 3.5.0
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-doSNOW >= 1.0.16

%description
Creating, refining, and clustering data nuggets. Data nuggets reduce a
large dataset into a small collection of nuggets of data, each containing
a center (location), weight (importance), and scale (variability)
parameter. Data nugget centers are created by choosing observations in the
dataset which are as equally spaced apart as possible. Data nugget weights
are created by counting the number observations closest to a given data
nugget’s center. We then say the data nugget 'contains' these observations
and the data nugget center is recalculated as the mean of these
observations. Data nugget scales are created by calculating the trace of
the covariance matrix of the observations contained within a data nugget
divided by the dimension of the dataset. Data nuggets are refined by
'splitting' data nuggets which have scales or shapes (defined as the ratio
of the two largest eigenvalues of the covariance matrix of the
observations contained within the data nugget) deemed too large. Data
nuggets are clustered by using a weighted form of k-means clustering which
uses both the centers and weights of data nuggets to optimize the
clustering assignments.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
