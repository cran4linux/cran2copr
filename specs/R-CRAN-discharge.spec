%global __brp_check_rpaths %{nil}
%global packname  discharge
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fourier Analysis of Discharge Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-lmom 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-boot 
Requires:         R-CRAN-lmom 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-checkmate 
Requires:         R-boot 

%description
Computes discrete fast Fourier transform of river discharge data and the
derived metrics. The methods are described in J. L. Sabo, D. M. Post
(2008) <doi:10.1890/06-1340.1> and J. L. Sabo, A. Ruhi, G. W. Holtgrieve,
V. Elliott, M. E. Arias, P. B. Ngor, T. A. Räsänsen, S. Nam (2017)
<doi:10.1126/science.aao1053>.

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
