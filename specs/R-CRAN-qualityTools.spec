%global packname  qualityTools
%global packver   1.55
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.55
Release:          3%{?dist}
Summary:          Statistical Methods for Quality Science

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-MASS 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Rsolnp 
Requires:         R-MASS 

%description
Contains methods associated with the Define, Measure, Analyze, Improve and
Control (i.e. DMAIC) cycle of the Six Sigma Quality Management
methodology.It covers distribution fitting, normal and non-normal process
capability indices, techniques for Measurement Systems Analysis especially
gage capability indices and Gage Repeatability (i.e Gage RR) and
Reproducibility studies, factorial and fractional factorial designs as
well as response surface methods including the use of desirability
functions. Improvement via Six Sigma is project based strategy that covers
5 phases: Define - Pareto Chart; Measure - Probability and
Quantile-Quantile Plots, Process Capability Indices for various
distributions and Gage RR Analyze i.e. Pareto Chart, Multi-Vari Chart, Dot
Plot; Improve - Full and fractional factorial, response surface and
mixture designs as well as the desirability approach for simultaneous
optimization of more than one response variable. Normal, Pareto and Lenth
Plot of effects as well as Interaction Plots; Control - Quality Control
Charts can be found in the 'qcc' package. The focus is on teaching the
statistical methodology used in the Quality Sciences.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
