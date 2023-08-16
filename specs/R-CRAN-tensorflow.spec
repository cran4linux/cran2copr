%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tensorflow
%global packver   2.13.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.13.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to 'TensorFlow'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.31
BuildRequires:    R-CRAN-tfruns >= 1.0
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-tfautograph >= 0.3.1
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-reticulate >= 1.31
Requires:         R-CRAN-tfruns >= 1.0
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-tfautograph >= 0.3.1
Requires:         R-CRAN-config 
Requires:         R-CRAN-processx 
Requires:         R-utils 
Requires:         R-CRAN-yaml 
Requires:         R-grDevices 

%description
Interface to 'TensorFlow' <https://www.tensorflow.org/>, an open source
software library for numerical computation using data flow graphs. Nodes
in the graph represent mathematical operations, while the graph edges
represent the multidimensional data arrays (tensors) communicated between
them. The flexible architecture allows you to deploy computation to one or
more 'CPUs' or 'GPUs' in a desktop, server, or mobile device with a single
'API'. 'TensorFlow' was originally developed by researchers and engineers
working on the Google Brain Team within Google's Machine Intelligence
research organization for the purposes of conducting machine learning and
deep neural networks research, but the system is general enough to be
applicable in a wide variety of other domains as well.

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
