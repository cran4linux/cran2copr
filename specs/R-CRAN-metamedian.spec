%global packname  metamedian
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          2%{?dist}
Summary:          Meta-Analysis of Medians

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-estmeansd 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-stats 
Requires:         R-CRAN-estmeansd 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-metafor 
Requires:         R-stats 

%description
Implements several methods to meta-analyze studies that report the sample
median of the outcome. When the primary studies are one-group studies, the
methods of McGrath et al. (2019) <doi:10.1002/sim.8013> can be applied to
estimate the pooled median. In the two-group context, the methods of
McGrath et al. (2020) <doi:10.1002/bimj.201900036> can be applied to
estimate the pooled raw difference of medians across groups.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
