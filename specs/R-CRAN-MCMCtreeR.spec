%global packname  MCMCtreeR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Prepare MCMCtree Analyses and Plot Bayesian Divergence TimeAnalyses Estimates on Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 3.0
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ape >= 3.0
Requires:         R-CRAN-sn 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Provides functions to prepare time priors for 'MCMCtree' analyses in the
'PAML' software from Yang (2007)<doi:10.1093/molbev/msm088> and plot
time-scaled phylogenies from any Bayesian divergence time analysis. Most
time-calibrated node prior distributions require user-specified
parameters. The package provides functions to refine these parameters, so
that the resulting prior distributions accurately reflect confidence in
known, usually fossil, time information. These functions also enable users
to visualise distributions and write 'MCMCtree' ready input files.
Additionally, the package supplies flexible functions to visualise age
uncertainty on a plotted tree with using node bars, using branch widths
proportional to the age uncertainty, or by plotting the full posterior
distributions on nodes. Time-scaled phylogenetic plots can be visualised
with absolute and geological timescales . All plotting functions are
applicable with output from any Bayesian software, not just 'MCMCtree'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
