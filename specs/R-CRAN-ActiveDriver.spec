%global __brp_check_rpaths %{nil}
%global packname  ActiveDriver
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Finding Cancer Driver Proteins with Enriched Mutations inPost-Translational Modification Sites

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-MASS 

%description
A mutation analysis tool that discovers cancer driver genes with frequent
mutations in protein signalling sites such as post-translational
modifications (phosphorylation, ubiquitination, etc). The Poisson
generalised linear regression model identifies genes where cancer
mutations in signalling sites are more frequent than expected from the
sequence of the entire gene. Integration of mutations with signalling
information helps find new driver genes and propose candidate mechanisms
to known drivers. Reference: Systematic analysis of somatic mutations in
phosphorylation signaling predicts novel cancer drivers. Juri Reimand and
Gary D Bader. Molecular Systems Biology (2013) 9:637
<doi:10.1038/msb.2012.68>.

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
