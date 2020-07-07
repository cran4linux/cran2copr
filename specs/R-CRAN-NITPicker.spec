%global packname  NITPicker
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Finds the Best Subset of Points to Sample

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fdasrvf 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fda.usc 
Requires:         R-CRAN-fdasrvf 
Requires:         R-CRAN-fda 
Requires:         R-stats 
Requires:         R-CRAN-fda.usc 

%description
Given a few examples of experiments over a time (or spatial) course,
'NITPicker' selects a subset of points to sample in follow-up experiments,
which would (i) best distinguish between the experimental conditions and
the control condition (ii) best distinguish between two models of how the
experimental condition might differ from the control (iii) a combination
of the two. Ezer and Keir (2018) <doi:10.1101/301796>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
