%global packname  EvaluateCore
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Quality Evaluation of Core Collections

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-kSamples 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-car 
Requires:         R-cluster 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-kSamples 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-vegan 

%description
Implements various quality evaluation statistics to assess the value of
plant germplasm core collections using qualitative and quantitative
phenotypic trait data according to Odong et al. (2015)
<doi:10.1007/s00122-012-1971-y>.

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
