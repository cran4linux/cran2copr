%global packname  aslib
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Interface to the Algorithm Selection Benchmark Library

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BatchExperiments 
BuildRequires:    R-CRAN-BatchJobs 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-llama 
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-parallelMap 
BuildRequires:    R-CRAN-ParamHelpers 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RWeka 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-BatchExperiments 
Requires:         R-CRAN-BatchJobs 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-llama 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-parallelMap 
Requires:         R-CRAN-ParamHelpers 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-RWeka 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-yaml 

%description
Provides an interface to the algorithm selection benchmark library at
<http://www.aslib.net> and the 'LLAMA' package
(<https://cran.r-project.org/package=llama>) for building algorithm
selection models; see Bischl et al. (2016)
<doi:10.1016/j.artint.2016.04.003>.

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

%files
%{rlibdir}/%{packname}
