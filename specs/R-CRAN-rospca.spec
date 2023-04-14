%global __brp_check_rpaths %{nil}
%global packname  rospca
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Robust Sparse PCA using the ROSPCA Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mrfDepth >= 1.0.5
BuildRequires:    R-CRAN-robustbase >= 0.92.6
BuildRequires:    R-CRAN-rrcovHD >= 0.2.3
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-elasticnet 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-mrfDepth >= 1.0.5
Requires:         R-CRAN-robustbase >= 0.92.6
Requires:         R-CRAN-rrcovHD >= 0.2.3
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-elasticnet 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pracma 

%description
Implementation of robust sparse PCA using the ROSPCA algorithm of Hubert
et al. (2016) <DOI:10.1080/00401706.2015.1093962>.

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
