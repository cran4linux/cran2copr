%global __brp_check_rpaths %{nil}
%global packname  SPPcomb
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Combining Different Spatial Datasets in Cancer Risk Estimation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-stats 
Requires:         R-CRAN-nleqslv 
Requires:         R-stats 

%description
We propose a novel two-step procedure to combine epidemiological data
obtained from diverse sources with the aim to quantify risk factors
affecting the probability that an individual develops certain disease such
as cancer. See Hui Huang, Xiaomei Ma, Rasmus Waagepetersen, Theodore R.
Holford, Rong Wang, Harvey Risch, Lloyd Mueller & Yongtao Guan (2014) A
New Estimation Approach for Combining Epidemiological Data From Multiple
Sources, Journal of the American Statistical Association, 109:505, 11-23,
<doi:10.1080/01621459.2013.870904>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
