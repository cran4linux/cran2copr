%global __brp_check_rpaths %{nil}
%global packname  funnelR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Funnel Plots for Proportion Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-stats 

%description
A set of simplified functions for creating funnel plots for proportion
data. This package supports user defined benchmarks, confidence limits and
estimation methods (i.e. exact or approximate) based on Spiegelhalter
(2005) <doi:10.1002/sim.1970>. Additional routines for returning scored
unit level data according to a set of specifications is also implemented
for convenience. Specifically, both a categorical and a continuous score
variable is returned to the sample data frame, which identifies which
observations are deemed extreme or in control. Typically, such variables
are useful as stratifications or covariates in further exploratory
analyses. Lastly, the plotting routine returns a base funnel plot
('ggplot2'), which can also be tailored.

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
