%global __brp_check_rpaths %{nil}
%global packname  tgcd
%global packver   2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5
Release:          3%{?dist}%{?buildtag}
Summary:          Thermoluminescence Glow Curve Deconvolution

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Deconvolving thermoluminescence glow curves according to various kinetic
models (first-order, second-order, general-order, and mixed-order) using a
modified Levenberg-Marquardt algorithm (More, 1978)
<DOI:10.1007/BFb0067700>. It provides the possibility of setting
constraints or fixing any of parameters. It offers an interactive way to
initialize parameters by clicking with a mouse on a plot at positions
where peak maxima should be located. The optimal estimate is obtained by
"trial-and-error". It also provides routines for simulating first-order,
second-order, and general-order glow peaks.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
