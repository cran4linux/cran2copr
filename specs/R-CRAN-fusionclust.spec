%global __brp_check_rpaths %{nil}
%global packname  fusionclust
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Clustering and Feature Screening using L1 Fusion Penalty

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.1
Requires:         R-core >= 3.4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-bbmle 
Requires:         R-stats 
Requires:         R-graphics 

%description
Provides the Big Merge Tracker and COSCI algorithms for convex clustering
and feature screening using L1 fusion penalty. See Radchenko, P. and
Mukherjee, G. (2017) <doi:10.1111/rssb.12226> and T.Banerjee et al. (2017)
<doi:10.1016/j.jmva.2017.08.001> for more details.

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
