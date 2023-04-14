%global __brp_check_rpaths %{nil}
%global packname  densratio
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Density Ratio Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Density ratio estimation. The estimated density ratio function can be used
in many applications such as anomaly detection, change-point detection,
covariate shift adaptation. The implemented methods are uLSIF (Hido et al.
(2011) <doi:10.1007/s10115-010-0283-2>), RuLSIF (Yamada et al. (2011)
<doi:10.1162/NECO_a_00442>), and KLIEP (Sugiyama et al. (2007)
<doi:10.1007/s10463-008-0197-x>).

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
