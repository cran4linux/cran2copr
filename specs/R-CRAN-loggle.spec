%global packname  loggle
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Local Group Graphical Lasso Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-glasso >= 1.8
BuildRequires:    R-CRAN-foreach >= 1.2.0
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-doParallel >= 1.0.8
BuildRequires:    R-CRAN-igraph >= 0.7
BuildRequires:    R-CRAN-sm 
Requires:         R-CRAN-glasso >= 1.8
Requires:         R-CRAN-foreach >= 1.2.0
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-doParallel >= 1.0.8
Requires:         R-CRAN-igraph >= 0.7
Requires:         R-CRAN-sm 

%description
Provides a set of methods that learn time-varying graphical models based
on data measured over a temporal grid. The underlying statistical model is
motivated by the needs to describe and understand evolving interacting
relationships among a set of random variables in many real applications,
for instance the study of how stocks interact with each other and how such
interactions change over time. The time-varying graphical models are
estimated under the assumption that the graph topology changes gradually
over time. For more details on estimating time-varying graphical models,
please refer to: Yang, J. & Peng, J. (2018) <arXiv:1804.03811>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
