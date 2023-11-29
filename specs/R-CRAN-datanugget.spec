%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datanugget
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Create, and Refine Data Nuggets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 4.0.5
BuildRequires:    R-CRAN-Rfast >= 2.0.7
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-doSNOW >= 1.0.16
Requires:         R-parallel >= 4.0.5
Requires:         R-CRAN-Rfast >= 2.0.7
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-doSNOW >= 1.0.16

%description
Creating, and refining data nuggets. Data nuggets reduce a large dataset
into a small collection of nuggets of data, each containing a center
(location), weight (importance), and scale (variability) parameter. Data
nugget centers are created by choosing observations in the dataset which
are as equally spaced apart as possible. Data nugget weights are created
by counting the number observations closest to a given data nugget’s
center. We then say the data nugget 'contains' these observations and the
data nugget center is recalculated as the mean of these observations. Data
nugget scales are created by calculating the trace of the covariance
matrix of the observations contained within a data nugget divided by the
dimension of the dataset. Data nuggets are refined by 'splitting' data
nuggets which have scales or shapes (defined as the ratio of the two
largest eigenvalues of the covariance matrix of the observations contained
within the data nugget) Reference paper: [1] Cherasia, K. E., Cabrera, J.,
Fernholz, L. T., & Fernholz, R. (2022). Data Nuggets in Supervised
Learning. emph{In Robust and Multivariate Statistical Methods:
Festschrift in Honor of David E. Tyler} (pp. 429-449). Cham: Springer
International Publishing. [2] Beavers, T., Cheng, G., Duan, Y., Cabrera,
J., Lubomirski, M., Amaratunga, D., Teigler, J. (2023). Data Nuggets: A
Method for Reducing Big Data While Preserving Data Structure (Submitted
for Publication).

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
