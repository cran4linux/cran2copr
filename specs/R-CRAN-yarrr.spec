%global packname  yarrr
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          A Companion to the e-Book "YaRrr!: The Pirate's Guide to R"

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-circlize 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-circlize 

%description
Contains a mixture of functions and data sets referred to in the
introductory e-book "YaRrr!: The Pirate's Guide to R". The latest version
of the e-book is available for free at
<https://www.thepiratesguidetor.com>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/appletv.jpg
%doc %{rlibdir}/%{packname}/basel.jpg
%doc %{rlibdir}/%{packname}/brave.jpg
%doc %{rlibdir}/%{packname}/bug.jpg
%doc %{rlibdir}/%{packname}/cars.jpg
%doc %{rlibdir}/%{packname}/compote.jpg
%doc %{rlibdir}/%{packname}/decision.jpg
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/eternal.jpg
%doc %{rlibdir}/%{packname}/evildead.jpg
%doc %{rlibdir}/%{packname}/fall.jpg
%doc %{rlibdir}/%{packname}/ghostbusters.jpg
%doc %{rlibdir}/%{packname}/harbor.jpg
%doc %{rlibdir}/%{packname}/iguana.jpg
%doc %{rlibdir}/%{packname}/malkovich.jpg
%doc %{rlibdir}/%{packname}/memento.jpg
%doc %{rlibdir}/%{packname}/monalisa.jpg
%doc %{rlibdir}/%{packname}/nemo.jpg
%doc %{rlibdir}/%{packname}/ohbrother.jpg
%doc %{rlibdir}/%{packname}/pebble.jpg
%doc %{rlibdir}/%{packname}/pony.jpg
%doc %{rlibdir}/%{packname}/rat.jpg
%doc %{rlibdir}/%{packname}/RReferenceCard.pdf
%doc %{rlibdir}/%{packname}/scholar.jpg
%doc %{rlibdir}/%{packname}/scuba.jpg
%doc %{rlibdir}/%{packname}/southpark.jpg
%doc %{rlibdir}/%{packname}/toystory.jpg
%doc %{rlibdir}/%{packname}/up.jpg
%doc %{rlibdir}/%{packname}/usualsuspects.jpg
%doc %{rlibdir}/%{packname}/xmen.jpg
%{rlibdir}/%{packname}/INDEX
