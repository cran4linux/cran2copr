%global packname  GWnnegPCA
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Geographically Weighted Non-Negative Principal ComponentsAnalysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-GWmodel 
BuildRequires:    R-CRAN-nsprcomp 
BuildRequires:    R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-GWmodel 
Requires:         R-CRAN-nsprcomp 
Requires:         R-methods 

%description
Implements a geographically weighted non-negative principal components
analysis, which consists of the fusion of geographically weighted and
sparse non-negative principal components analyses (Tsutsumida N. et al.,
(2019) <doi:10.17608/k6.auckland.9850826.v1>).

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
