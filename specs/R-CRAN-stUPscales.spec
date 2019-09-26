%global packname  stUPscales
%global packver   1.0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3.4
Release:          1%{?dist}
Summary:          Spatio-Temporal Uncertainty Propagation Across Multiple Scales

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mAr 
BuildRequires:    R-CRAN-lmom 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-hydroGOF 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-EmiStatR 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-mAr 
Requires:         R-CRAN-lmom 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-lattice 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-hydroGOF 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-EmiStatR 

%description
Integrated environmental modelling requires coupling sub-models at
different spatial and temporal scales, thus accounting for change of
support procedures (aggregation and disaggregation). We contribute to
state-of-the-art open source tools that support uncertainty propagation
analysis in temporal and spatio-temporal domains. We implement the tool
for uncertainty propagation in environmental modelling, with examples in
the urban water domain. The functionalities of the class setup and the
methods and functions MC.setup, MC.sim, MC.analysis, MC.analysis_generic
and Agg.t are contained, which are used for setting up, running and
analysing Monte Carlo uncertainty propagation simulations, and for
spatio-temporal aggregation. We also implement functionalities to model
and predict variables that vary in space and time. stUPscales takes
uncertainty characterisation and propagation a step further by including
temporal and spatio-temporal auto- and cross-correlation, resulting in
more realistic (spatio-)temporal series of environmental variables. Due to
its modularity, the package allows the implementation of additional
methods and functions for spatio-temporal disaggregation of model inputs
and outputs, when linking models across multiple space-time scales.

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
