%global __brp_check_rpaths %{nil}
%global packname  rSHAPE
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulated Haploid Asexual Population Evolution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-evd 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
In silico experimental evolution offers a cost-and-time effective means to
test evolutionary hypotheses.  Existing evolutionary simulation tools
focus on simulations in a limited experimental framework, and tend to
report on only the results presumed of interest by the tools designer.
The R-package for Simulated Haploid Asexual Population Evolution
('rSHAPE') addresses these concerns by implementing a robust simulation
framework that outputs complete population demographic and genomic
information for in silico evolving communities.  Allowing more than 60
parameters to be specified, 'rSHAPE' simulates evolution across discrete
time-steps for an evolving community of haploid asexual populations with
binary state genomes.  These settings are for the current state of
'rSHAPE' and future steps will be to increase the breadth of evolutionary
conditions permitted.  At present, most effort was placed into permitting
varied growth models to be simulated (such as constant size, exponential
growth, and logistic growth) as well as various fitness landscape models
to reflect the evolutionary landscape (e.g.: Additive, House of Cards -
Stuart Kauffman and Simon Levin (1987)
<doi:10.1016/S0022-5193(87)80029-2>, NK - Stuart A. Kauffman and Edward D.
Weinberger (1989) <doi:10.1016/S0022-5193(89)80019-0>, Rough Mount Fuji -
Neidhart, Johannes and Szendro, Ivan G and Krug, Joachim (2014)
<doi:10.1534/genetics.114.167668>). This package includes numerous
functions though users will only need defineSHAPE(), runSHAPE(),
shapeExperiment() and summariseExperiment().  All other functions are
called by these main functions and are likely only to be on interest for
someone wishing to develop 'rSHAPE'.  Simulation results will be stored in
files which are exported to the directory referenced by the shape_workDir
option (defaults to tempdir() but do change this by passing a folderpath
argument for workDir when calling defineSHAPE() if you plan to make use of
your results beyond your current session).  'rSHAPE' will generate
numerous replicate simulations for your defined range of experimental
parameters.  The experiment will be built under the experimental working
directory (i.e.: referenced by the option shape_workDir set using
defineSHAPE() ) where individual replicate simulation results will be
stored as well as processed results which I have made in an effort to
facilitate analyses by automating collection and processing of the
potentially thousands of files which will be created. On that note,
'rSHAPE' implements a robust and flexible framework with highly detailed
output at the cost of computational efficiency and potentially requiring
significant disk space (generally gigabytes but up to tera-bytes for very
large simulation efforts).  So, while 'rSHAPE' offers a single framework
in which we can simulate evolution and directly compare the impacts of a
wide range of parameters, it is not as quick to run as other in silico
simulation tools which focus on a single scenario with limited output.
There you have it, 'rSHAPE' offers you a less restrictive in silico
evolutionary playground than other tools and I hope you enjoy testing your
hypotheses.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
