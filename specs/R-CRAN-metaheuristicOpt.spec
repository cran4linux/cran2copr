%global packname  metaheuristicOpt
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          2%{?dist}
Summary:          Metaheuristic for Optimization

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
An implementation of metaheuristic algorithms for continuous optimization.
Currently, the package contains the implementations of 21 algorithms, as
follows: particle swarm optimization (Kennedy and Eberhart, 1995), ant
lion optimizer (Mirjalili, 2015 <doi:10.1016/j.advengsoft.2015.01.010>),
grey wolf optimizer (Mirjalili et al., 2014
<doi:10.1016/j.advengsoft.2013.12.007>), dragonfly algorithm (Mirjalili,
2015 <doi:10.1007/s00521-015-1920-1>), firefly algorithm (Yang, 2009
<doi:10.1007/978-3-642-04944-6_14>), genetic algorithm (Holland, 1992,
ISBN:978-0262581110), grasshopper optimisation algorithm (Saremi et al.,
2017 <doi:10.1016/j.advengsoft.2017.01.004>), harmony search algorithm
(Mahdavi et al., 2007 <doi:10.1016/j.amc.2006.11.033>), moth flame
optimizer (Mirjalili, 2015 <doi:10.1016/j.knosys.2015.07.006>, sine cosine
algorithm (Mirjalili, 2016 <doi:10.1016/j.knosys.2015.12.022>), whale
optimization algorithm (Mirjalili and Lewis, 2016
<doi:10.1016/j.advengsoft.2016.01.008>), clonal selection algorithm
(Castro, 2002 <doi:10.1109/TEVC.2002.1011539>), differential evolution
(Das & Suganthan, 2011), shuffled frog leaping (Eusuff, Landsey & Pasha,
2006), cat swarm optimization (Chu et al., 2006), artificial bee colony
algorithm (Karaboga & Akay, 2009), krill-herd algorithm (Gandomi & Alavi,
2012), cuckoo search (Yang & Deb, 2009), bat algorithm (Yang, 2012),
gravitational based search (Rashedi et al., 2009) and black hole
optimization (Hatamlou, 2013).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
