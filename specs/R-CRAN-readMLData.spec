%global packname  readMLData
%global packver   0.9-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          3%{?dist}%{?buildtag}
Summary:          Reading Machine Learning Benchmark Data Sets in DifferentFormats

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-XML 

%description
Functions for reading data sets in different formats for testing machine
learning tools are provided. This allows to run a loop over several data
sets in their original form, for example if they are downloaded from UCI
Machine Learning Repository. The data are not part of the package and have
to be downloaded separately.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/exampleData
%doc %{rlibdir}/%{packname}/exampleDescription
%{rlibdir}/%{packname}/INDEX
