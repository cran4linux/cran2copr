%global __brp_check_rpaths %{nil}
%global packname  IBDsim
%global packver   0.9-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          3%{?dist}%{?buildtag}
Summary:          Simulation of Chromosomal Regions Shared by Family Members

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-paramlink >= 1.1
BuildRequires:    R-stats 
Requires:         R-CRAN-paramlink >= 1.1
Requires:         R-stats 

%description
Simulation of segments shared identical-by-descent (IBD) by pedigree
members. Using sex specific recombination rates along the human genome
(Kong et. al (2010) <doi:10.1038/nature09525>), phased chromosomes are
simulated for all pedigree members, either by unconditional gene dropping
or conditional on a specified IBD pattern. Additional functions provide
summaries and further analysis of the simulated genomes.

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
