%global __brp_check_rpaths %{nil}
%global packname  wISAM
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          3%{?dist}%{?buildtag}
Summary:          Weighted Inbred Strain Association Mapping

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
Requires:         R-methods 
Requires:         R-MASS 

%description
In the course of a genome-wide association study, the situation often
arises that some phenotypes are known with greater precision than others.
It could be that some individuals are known to harbor more
micro-environmental variance than others. In the case of inbred strains of
model organisms, it could be the case that more organisms were observed
from some strains than others, so the strains with more organisms have
better-estimated means. Package 'wISAM' handles this situation by allowing
for weighting of each observation according to residual variance.
Specifically, the 'weight' parameter to the function conduct_scan() takes
the precision of each observation (one over the variance).

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
