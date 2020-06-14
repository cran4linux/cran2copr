%global packname  hpcwld
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          2%{?dist}
Summary:          High Performance Cluster Models Based on Kiefer-WolfowitzRecursion

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-multicool 
BuildRequires:    R-CRAN-partitions 
Requires:         R-CRAN-multicool 
Requires:         R-CRAN-partitions 

%description
Probabilistic models describing the behavior of workload and queue on a
High Performance Cluster and computing GRID under FIFO service discipline
basing on modified Kiefer-Wolfowitz recursion. Also sample data for
inter-arrival times, service times, number of cores per task and waiting
times of HPC of Karelian Research Centre are included, measurements took
place from 06/03/2009 to 02/30/2011. Functions provided to import/export
workload traces in Standard Workload Format (swf). Stability condition of
the model may be verified either exactly, or approximately.

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
