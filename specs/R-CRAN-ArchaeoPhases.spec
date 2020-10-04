%global packname  ArchaeoPhases
%global packver   1.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.5
Release:          3%{?dist}%{?buildtag}
Summary:          Post-Processing of the Markov Chain Simulated by 'ChronoModel','Oxcal' or 'BCal'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-hdrcde 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-toOrdinal 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggalt 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-hdrcde 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-toOrdinal 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggalt 

%description
Provides a list of functions for the statistical analysis of
archaeological dates and groups of dates (see <doi:10.18637/jss.v093.c01>
for a description). It is based on the post-processing of the Markov
Chains whose stationary distribution is the posterior distribution of a
series of dates. Such output can be simulated by different applications as
for instance 'ChronoModel' (see <http://www.chronomodel.fr>), 'Oxcal' (see
<https://c14.arch.ox.ac.uk/oxcal.html>) or 'BCal' (see
<http://bcal.shef.ac.uk/>). The only requirement is to have a csv file
containing a sample from the posterior distribution.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
