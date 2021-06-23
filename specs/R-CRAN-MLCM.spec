%global __brp_check_rpaths %{nil}
%global packname  MLCM
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Conjoint Measurement

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-base 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-base 

%description
Conjoint measurement is a psychophysical procedure in which stimulus pairs
are presented that vary along 2 or more dimensions and the observer is
required to compare the stimuli along one of them.  This package contains
functions to estimate the contribution of the n scales to the judgment by
a maximum likelihood method under several hypotheses of how the perceptual
dimensions interact. Reference: Knoblauch & Maloney (2012) "Modeling
Psychophysical Data in R". <doi:10.1007/978-1-4614-4475-6>.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/ToDo
%{rlibdir}/%{packname}/INDEX
