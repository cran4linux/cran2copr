%global packname  iemisctext
%global packver   0.9.99
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.99
Release:          2%{?dist}
Summary:          Irucka Embry's Miscellaneous Text Collection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch

%description
The eclectic collection includes the following written pieces: "The War
Prayer" by Mark Twain, "War Is A Racket" by Major General Smedley Butler,
"The Mask of Anarchy: Written on the Occasion of the Massacre at
Manchester" by Percy Bysshe Shelley, "Connect the D.O.T.S." by Obiora
Embry, "Untitled: Climate Strange" by Irucka Ajani Embry, and "Untitled:
Us versus Them or People Screwing over Other People (as we all live on one
Earth and there is no "us versus them" in the actual Ultimate Reality}" by
Irucka Ajani Embry.

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
%doc %{rlibdir}/%{packname}/COPYRIGHT
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/texts
%{rlibdir}/%{packname}/INDEX
