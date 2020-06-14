%global packname  foreSIGHT
%global packver   0.9.81
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.81
Release:          2%{?dist}
Summary:          Systems Insights from Generation of Hydroclimatic Timeseries

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GA >= 3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-directlabels 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-moments 
Requires:         R-CRAN-GA >= 3.0
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-directlabels 
Requires:         R-CRAN-cowplot 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-moments 

%description
A tool to create hydroclimate scenarios, stress test systems and visualize
system performance in scenario-neutral climate change impact assessments.
Scenario-neutral approaches 'stress-test' the performance of a modelled
system by applying a wide range of plausible hydroclimate conditions (see
Brown & Wilby (2012) <doi:10.1029/2012EO410001> and Prudhomme et al.
(2010) <doi:10.1016/j.jhydrol.2010.06.043>). These approaches allow the
identification of hydroclimatic variables that affect the vulnerability of
a system to hydroclimate variation and change. This tool enables the
generation of perturbed time series using a range of approaches including
simple scaling of observed time series (e.g. Culley et al. (2016)
<doi:10.1002/2015WR018253>) and stochastic simulation of perturbed time
series via an inverse approach (see Guo et al. (2018)
<doi:10.1016/j.jhydrol.2016.03.025>). It incorporates a number of
stochastic weather models to generate hydroclimate variables on a daily
basis (e.g. precipitation, temperature, potential evapotranspiration) and
allows a variety of different hydroclimate variable properties, herein
called attributes, to be perturbed. Options are included for the easy
integration of existing system models both internally in R and externally
for seamless 'stress-testing'. A suite of visualization options for the
results of a scenario-neutral analysis (e.g. plotting performance spaces
and overlaying climate projection information) are also included. As
further developments in scenario-neutral approaches occur the tool will be
updated to incorporate these advances.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
