%global __brp_check_rpaths %{nil}
%global packname  clampSeg
%global packver   1.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Idealisation of Patch Clamp Recordings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stepR >= 2.1.0
BuildRequires:    R-CRAN-lowpassFilter 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-stepR >= 2.1.0
Requires:         R-CRAN-lowpassFilter 
Requires:         R-stats 
Requires:         R-methods 

%description
Implements the model-free multiscale idealisation approaches:
Jump-Segmentation by MUltiResolution Filter (JSMURF)
<doi:10.1109/TNB.2013.2284063>, JUmp Local dEconvolution Segmentation
filter (JULES) <doi:10.1109/TNB.2018.2845126> and Heterogeneous
Idealization by Local testing and DEconvolution (HILDE)
<arXiv:2008.02658>. Further details on how to use them are given in the
accompanying vignette.

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
